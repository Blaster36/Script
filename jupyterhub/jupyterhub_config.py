#c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'
c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'
c.LDAPAuthenticator.valid_username_regex = r'^[a-z0-9][.a-z0-9_-]*$'
c.LDAPAuthenticator.use_ssl = False
c.LDAPAuthenticator.server_address = '172.18.0.1'
c.LDAPAuthenticator.server_port = 389
c.LDAPAuthenticator.bind_dn_template = 'uid={username},ou=people,ou=jhub,dc=dapf,dc=smbc,dc=local'
c.LDAPAuthenticator.lookup_dn = False

#c.JupyterHub.db_url = 'sqlite:////etc/jupyterhub/jupyterhub.sqlite'
c.JupyterHub.hub_connect_ip = 'jupyterhub'
c.JupyterHub.hub_ip = '0.0.0.0'
#c.JupyterHub.hub_port = 8081
#c.JupyterHub.ip = '127.0.0.1'
c.Authenticator.admin_users = {'jupyter', 'admin'}

from dockerspawner import DockerSpawner

class DemoFormSpawner(DockerSpawner):
  def _options_form_default(self):
    default_stack = 'jupyter/minimal-notebook(w/MeCab)'
    return """
    <label for="stack">Select your desired stack</label>
    <select name="stack" size="1">
      <option value="jupyter/minimal-notebook:9e8682c9ea54-MeCab">jupyter/minimal-notebook(w/MeCab)</option>
      <option value="jupyter/minimal-notebook:9e8682c9ea54-MeCab-Slum">jupyter/minimal-notebook(w/MeCab/Selenium)</option>
      <option value="nvcr.io/nvidia/tensorflow:20.11-tf2-py3-gpu">nvcr.io/nvidia/tensorflow(w/Hub)</option>
      <option value="nvcr.io/nvidia/pytorch:20.11-py3-gpu">nvcr.io/nvidia/pytorch(w/Hub)</option>
      <option value="jupyter/minimal-notebook:python-3.8.8">jupyter/minimal-notebook(py3.8)</option>
      <option value="quay.io/thoth-station/s2i-minimal-py38-notebook:v0.2.2">jupyter/s2i-minimal-notebook(py3.8)</option>
      <option value="quay.io/thoth-station/s2i-minimal-py38-notebook:v1.0.0">jupyter/s2i-minimal-notebook(py3.8 w/MeCab)</option>
    </select>
    """.format(stack=default_stack)

  def options_from_form(self, formdata):
    options = {}
    options['stack'] = formdata['stack']
    container_image = ''.join(formdata['stack'])
    print('SPAWN: ' + container_image + 'IMAGE')
    self.image = container_image
    return options

#c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.JupyterHub.spawner_class = DemoFormSpawner

notebook_dir = '/home/jovyan'
c.DemoFormSpawner.notebook_dir = notebook_dir
c.DemoFormSpawner.volumes = {'jupyterhub-user-{username}':notebook_dir}
c.DemoFormSpawner.remove = True
c.DemoFormSpawner.default_url = '/lab'
c.DemoFormSpawner.start_timeout = 300
c.DemoFormSpawner.http_timeout = 120
c.DemoFormSpawner.network_name = 'jupyterhub'
