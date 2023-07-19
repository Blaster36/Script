from jupyter_client.localinterfaces import public_ips
ip = public_ips()[0]

c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'
#c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'
#c.LDAPAuthenticator.valid_username_regex = r'^[a-z0-9][.a-z0-9_-]*$'
#c.LDAPAuthenticator.use_ssl = False
#c.LDAPAuthenticator.server_address = '192.168.130.200'
#c.LDAPAuthenticator.server_port = 389
#c.LDAPAuthenticator.bind_dn_template = 'uid={username},ou=people,ou=jhub,dc=dapf,dc=com'
#c.LDAPAuthenticator.lookup_dn = False

#c.JupyterHub.db_url = 'sqlite:////etc/jupyterhub/jupyterhub.sqlite'
#c.JupyterHub.hub_connect_ip = 'jupyterhub'
#c.JupyterHub.hub_ip = '192.168.130.200'
c.JupyterHub.hub_ip = ip
#c.JupyterHub.hub_port = 8081
#c.JupyterHub.ip = '127.0.0.1'
c.JupyterHub.ip = ip
c.Authenticator.admin_users = {'jupyter', 'admin'}

c.ServerApp.iopub_data_rate_limit = 100000000.0
c.ServerApp.rate_limit_window = 1.0

from dockerspawner import DockerSpawner
#from podmanclispawner import PodmanCLISpawner
import os

class DemoFormSpawner(DockerSpawner):
  def _options_form_default(self):
    default_stack = 'thoth-station/s2i-minimal-notebook(Python 3.8)'
    return """
    <label for="stack">Select your desired stack</label>
    <select name="stack" size="1">
      <option value="jupyter/minimal-notebook:python-3.8.8">jupyter/minimal-notebook(Python 3.8)</option>
      <option value="jupyter/minimal-notebook:python-3.8.8-podman">jupyter/minimal-notebook(Python 3.8 w/jupyterhub==3.1.1)</option>
      <option value="quay.io/jupyteronopenshift/s2i-minimal-notebook-py36:2.5.1">jupyteronopenshift/s2i-minimal-notebook(Python 3.6)</option>
      <option value="quay.io/thoth-station/s2i-minimal-py38-notebook:v1.0.0">thoth-station/s2i-minimal-notebook(Python 3.8)</option>
    </select>
    """.format(stack=default_stack)

  def options_from_form(self, formdata):
    options = {}
    options['stack'] = formdata['stack']
    container_image = ''.join(formdata['stack'])
    print('SPAWN: ' + container_image + 'IMAGE')
    self.image = container_image
    self.log.info( "<<options_from_form>> %s", self.image)
    return options

  def start(self):
    self.log.info( "<<start>> %s", self.image)
    notebook_dir = '/home/jovyan'
    if self.image == 'quay.io/jupyteronopenshift/s2i-minimal-notebook-py36:2.5.1':
       notebook_dir = '/opt/app-root/src'
    elif self.image == 'quay.io/thoth-station/s2i-minimal-py38-notebook:v1.0.0':
       notebook_dir = '/opt/app-root/src'
    else:
       notebook_dir = '/home/jovyan'
    self.notebook_dir = notebook_dir
    self.volumes = {'jupyterhub-user-{username}':notebook_dir}
    self.volumes['jupyterhub-user-{username}'] = notebook_dir + '/work'
    self.log.info( "<<start self.volumes>> %s", self.volumes)
    return super().start()

#c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
#c.JupyterHub.spawner_class = 'podmancli'
c.JupyterHub.spawner_class = DemoFormSpawner

#notebook_dir = '/home/jovyan'
#c.DemoFormSpawner.notebook_dir = notebook_dir
#c.DemoFormSpawner.volumes = {'jupyterhub-user-{username}':notebook_dir}
c.DemoFormSpawner.remove = True
c.DemoFormSpawner.default_url = '/lab'
c.DemoFormSpawner.start_timeout = 300
c.DemoFormSpawner.http_timeout = 120
c.DemoFormSpawner.network_name = 'jupyterhub'
c.DemoFormSpawner.debug = True

