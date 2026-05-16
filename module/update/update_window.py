from __future__ import annotations

import os
import subprocess

from module.localization import tr
from module.update.update_engine import build_independent_process_env


def launch_updater(wait_pid: int) -> None:
    """启动独立更新器 March7th Updater.exe，传入主进程 PID。"""
    source_file = os.path.abspath("./March7th Updater.exe")
    if not os.path.exists(source_file):
        raise FileNotFoundError(tr("未找到更新程序"))

    creationflags = (
        getattr(subprocess, "DETACHED_PROCESS", 0)
        | getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
    )
    command = [source_file, "--mode", "full", "--wait-pid", str(wait_pid)]
    subprocess.Popen(
        command,
        creationflags=creationflags,
        env=build_independent_process_env(),
        close_fds=True,
    )