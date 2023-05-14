    from jupyterhub.auth import DummyAuthenticator
    c.JupyterHub.authenticator_class = DummyAuthenticator
    c.DummyAuthenticator.auto_login = False
    c.KubeSpawner.environment = { "JUPYTER_ENABLE_LAB": "true" }
    c.KubeSpawner.start_timeout = 300
    c.KubeSpawner.http_timeout = 120
    c.Authenticator.admin_users = { "admin", "jupyter" }
    c.KubeSpawner.profile_list = [
        {
            "display_name": "Python 3.6",
            "description": "[Resource] CPU:1.0/Mem:4.0GB",
            "default": True,
            "kubespawner_override": {
                "image": "s2i-minimal-notebook-py36:2.5.1",
                "cpu_guarantee": 1.0,
                "cpu_limit": 1.0,
                "mem_guarantee": "4000M",
                "mem_limit": "4000M",
            }
        },
        {
            "display_name": "Python 3.8",
            "description": "[Resource] CPU:1.0/Mem:4.0GB",
            "kubespawner_override": {
                "image": "s2i-minimal-py38-notebook:v1.0.0",
                "cpu_guarantee": 1.0,
                "cpu_limit": 1.0,
                "mem_guarantee": "4000M",
                "mem_limit": "4000M",
            }
        },
        {
            "display_name": "Python 3.8 w/Spark",
            "description": "[Resource] CPU:1.0/Mem:4.0GB",
            "kubespawner_override": {
                "image": "pyspark-notebook:python-3.8",
                'supplemental_gids': [100],
                "cpu_guarantee": 1.0,
                "cpu_limit": 1.0,
                "mem_guarantee": "4000M",
                "mem_limit": "4000M",
                "volume_mounts": [
                  {
                    "name": "data",
                    "mountPath": "/home/jovyan"
                  },
                  {
                    "name": "shared",
                    "mountPath": "/home/shared"
                  }
                ]
            }
        }
    ]
    c.KubeSpawner.pvc_name_template = "pvc-{username}"
    c.KubeSpawner.user_storage_capacity = "1Gi"
    c.KubeSpawner.volumes = [
        {
            "name": "data",
            "persistentVolumeClaim": {
                "claimName": c.KubeSpawner.pvc_name_template
            }
        },
        {
            "name": "shared",
            "persistentVolumeClaim": {
                "claimName": "pvc-sharedrwx"
            }
        }
    ]
    c.KubeSpawner.volume_mounts = [
        {
            "name": "data",
            "mountPath": "/opt/app-root/src"
        },
        {
            "name": "shared",
            "mountPath": "/opt/app-root/shared"
        }
    ]
