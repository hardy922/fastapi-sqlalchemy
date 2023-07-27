# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/7/22 9:44
# @File: linux.py
# @Software: PyCharm

import paramiko
from app.utils import log



class LinuxOpt(object):

    @classmethod
    async def init(cls):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname='x.x.x.x', port=22,
                    username='root', password='password')
        return ssh

    @classmethod
    async def exec_commands(cls, cmd):
        ssh = await cls.init()
        try:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            result = str(stdout.read(), encoding='utf-8')
            status = stdout.channel.recv_exit_status()
            if status:
                log.warning(f'执行命令{cmd}出错-->{stderr.read()}')
                out = False
            else:
                out = result
            ssh.close()
            return out
        except Exception as e:
            log.error(f'执行命令{cmd} 出错-->{str(e)}')
            ssh.close()
            return False

    @classmethod
    async def sftp_file(cls, remote_path):
        """
        获取文件
        """
        try:
            ssh = await cls.init()
            with ssh.open_sftp() as sftp:
                remote_file = sftp.file(remote_path)
            return remote_file, ssh
        except Exception as e:
            log.error(f'获取文件{remote_path}出错-->{str(e)}')
            return False
