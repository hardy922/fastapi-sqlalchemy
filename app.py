
import argparse
import uvicorn
from app import create_app
from app.utils import log
from version import version

app = create_app()


def parse_args():
    parser = argparse.ArgumentParser(description='run app')
    parser.add_argument('-i', '--ip', default='127.0.0.1', help='ip address to run app on.')
    parser.add_argument('-p', '--port', type=int, default=5002, help='port to run app on.')
    parser.add_argument('-r', '--reload', action='store_true', help='enable auto-reloading.')
    parser.add_argument('-l', '--log-level', default='info', choices=['debug', 'info', 'warning', 'error'],
                        help='log level.')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    log.info(f'启动服务版本：{version}......')
    uvicorn.run("app:app", host=args.ip, port=args.port, reload=args.reload, log_level=args.log_level)

