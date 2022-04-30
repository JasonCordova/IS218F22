import os

def test_log_directory():

    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, '../app/logs')

    assert os.path.exists(logdir) == True

def test_log_file():
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    log_file = os.path.join(root, '../app/logs/info.log')
    print(log_file)

    assert os.path.exists(log_file) == True