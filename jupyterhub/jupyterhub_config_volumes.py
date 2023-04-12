#c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'
c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'
c.LDAPAuthenticator.valid_username_regex = r'^[a-z0-9][.a-z0-9_-]*$'
c.LDAPAuthenticator.use_ssl = False
c.LDAPAuthenticator.server_address = '172.17.0.1'
c.LDAPAuthenticator.server_port = 389
c.LDAPAuthenticator.bind_dn_template = 'uid={username},ou=people,ou=jhub,dc=dapf,dc=com'
c.LDAPAuthenticator.lookup_dn = False

#c.JupyterHub.db_url = 'sqlite:////etc/jupyterhub/jupyterhub.sqlite'
c.JupyterHub.hub_connect_ip = 'jupyterhub'
c.JupyterHub.hub_ip = '0.0.0.0'
#c.JupyterHub.hub_port = 8081
#c.JupyterHub.ip = '127.0.0.1'
c.Authenticator.admin_users = {'jupyter', 'admin'}

c.ServerApp.iopub_data_rate_limit = 100000000.0
c.ServerApp.rate_limit_window = 1.0

from dockerspawner import DockerSpawner
import os

class DemoFormSpawner(DockerSpawner):
  def _options_form_default(self):
    default_stack = 'jupyter/s2i-minimal-notebook(Python 3.6)'
    return """
    <label for="stack">Select your desired stack</label>
    <select name="stack" size="1">
      <option value="quay.io/jupyteronopenshift/s2i-minimal-notebook-py36:2.5.1">jupyter/s2i-minimal-notebook(Python 3.6)</option>
      <option value="quay.io/thoth-station/s2i-minimal-py38-notebook:v1.0.0">jupyter/s2i-minimal-notebook(Python 3.8)</option>
      <option value="quay.io/thoth-station/s2i-minimal-py38-notebook:v1.0.0-MeCab">jupyter/s2i-minimal-notebook(Python 3.8 w/MeCab)</option>
      <option value="jupyter/minimal-notebook:python-3.8.8">jupyter/minimal-notebook(Python 3.8)</option>
      <option value="jupyter/minimal-notebook:python-3.8.8-TALib">jupyter/minimal-notebook(Python 3.8 w/TALib)</option>
      <option value="jupyter/minimal-notebook:python-3.9.13">jupyter/minimal-notebook(Python 3.9)</option>
      <option value="jupyter/pyspark-notebook:python-3.8">jupyter/minimal-notebook(Python 3.8 w/Spark)</option>
      <option value="nvidia/cuda:11.4.0-cudnn8-devel-ubuntu20.04-lab">nvidia/cuda(CUDA 11.4)</option>
      <option value="pycaret/full:python-3.8.16">pycaret/full(Python 3.8)</option>
      <option value="test:v1.0.0">test(for CustomImage)</option>
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
    elif self.image == 'quay.io/thoth-station/s2i-minimal-py38-notebook:v1.0.0-MeCab':
       notebook_dir = '/opt/app-root/src'
    else:
       notebook_dir = '/home/jovyan'
    self.notebook_dir = notebook_dir
    #self.volumes = {'jupyterhub-user-{username}':notebook_dir}
    self.volumes['jupyterhub-user-{username}'] = notebook_dir + '/work'
    self.log.info( "<<start self.volumes>> %s", self.volumes)
    return super().start()

#c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
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
