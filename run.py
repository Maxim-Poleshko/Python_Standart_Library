from utils.task1 import make_dirs, dir_tree_func
from utils.task2 import study_group
from utils.task3 import save_img
from utils.members import list_members

MY_PATH = "/home/max/forcoding/"
make_dirs(MY_PATH)
dir_tree_func(MY_PATH)

study_group(list_members)

save_img()
