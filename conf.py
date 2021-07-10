def __init__(self):
        self.ssh_output = None
        self.ssh_error = None
        self.client = None
        self.host= conf_file.HOST
        self.username = conf_file.USERNAME
        self.password = conf_file.PASSWORD
        self.timeout = float(conf_file.TIMEOUT)
        self.commands = conf_file.COMMANDS
        self.pkey = conf_file.PKEY
        self.port = conf_file.PORT
        self.uploadremotefilepath = conf_file.UPLOADREMOTEFILEPATH
        self.uploadlocalfilepath = conf_file.UPLOADLOCALFILEPATH
        self.downloadremotefilepath = conf_file.DOWNLOADREMOTEFILEPATH
        self.downloadlocalfilepath = conf_file.DOWNLOADLOCALFILEPATH
