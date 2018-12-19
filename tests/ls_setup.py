##########################################################################
# Copyright (c) Open Law Library. All rights reserved.                   #
# See ThirdPartyNotices.txt in the project root for license information. #
##########################################################################
import threading

from tests import (CMD_ASYNC, CMD_SYNC, CMD_THREAD, FEATURE_ASYNC,
                   FEATURE_SYNC, FEATURE_THREAD)


def setup_ls_features(server):

    # Commands
    @server.command(CMD_ASYNC)
    async def cmd_test3(ls, *args):  # pylint: disable=unused-variable
        return True, threading.get_ident()

    @server.thread()
    @server.command(CMD_THREAD)
    def cmd_test1(ls, *args):  # pylint: disable=unused-variable
        return True, threading.get_ident()

    @server.command(CMD_SYNC)
    def cmd_test2(ls, *args):  # pylint: disable=unused-variable
        return True, threading.get_ident()

    # Features
    @server.feature(FEATURE_ASYNC)
    async def feature_async(ls, *args):  # pylint: disable=unused-variable
        return True, threading.get_ident()

    @server.feature(FEATURE_SYNC)
    def feature_sync(ls, *args):  # pylint: disable=unused-variable
        return True, threading.get_ident()

    @server.feature(FEATURE_THREAD)
    @server.thread()
    def feature_thread(ls, *args):  # pylint: disable=unused-variable
        return True, threading.get_ident()