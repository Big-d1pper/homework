import json
import os
import pickle
import re
#
# text = """
# Wqweqwe sadasd Loki sda sd Dess. Some other Name."
# """
# if __name__ == '__main__':
#     print(re.findall(r'[^\.] ([A-Z][a-z]+)', text))

# text = "123.123 safd sad asd ad 234.234.234.234"
#
# if __name__ == '__main__':
#     match = re.match(
#         "(?P<first_part>\d+).(?P<second_part>\d+)", text)
#     print(match.groupdict())


# def some_method_1():
#     some_lst_1 = list(range(0, 10000000))
#     print(some_lst_1)
#     with open('my_pickle', 'wb') as file:
#         pickle.dump(some_lst_1, file)
#
#
# def some_method_2():
#     with open('my_pickle', 'rb') as file:
#         some_lst_1 = pickle.load(file)
#         print(some_lst_1)


# if __name__ == '__main__':
#     some_method_1()
#     some_method_2()

# with open('my_pickle', 'rb') as file:
#     some_lst_1 = pickle.load(file)
#     print(some_lst_1)

# def some_method_1():
#     some_dict_1 = [{
#         "name": "Loki",
#         "age": 29
#     },
#         {
#             "name": "Odin",
#             "age": "endless"
#         },
#         {
#             "name": "Tor",
#             "age": 12
#         }
#     ]
#     print(some_dict_1)
#     with open('my_file.json', 'w') as file:
#         json.dump(some_dict_1, file, indent=4)
#
#
# def some_method_2():
#     with open('my_file.json', 'r') as file:
#         some_dict_1 = json.load(file)
#         print(some_dict_1)
#
#
# if __name__ == '__main__':
#     some_method_1()
#     some_method_2()


# def some_method(count):
#     print(count)
#     count += 1
#     if count == 100:
#         return
#     some_method(count)
#
#
# some_method(0)
import time


def cache(filename=None):

    def wrapped_wrapper(method):

        def wrapper(*args, **kwargs):

            if not filename:
                file_name = f'{"_".join([str(x) for x in args])}.cache'
            else:
                file_name = filename

            if os.path.exists(file_name):
                with open(file_name, 'rb') as file:
                    return pickle.load(file)
            else:
                with open(file_name, 'wb') as file:
                    result = method(*args, **kwargs)
                    pickle.dump(result, file)
                return result

        return wrapper

    return wrapped_wrapper


if __name__ == '__main__':
    @cache(filename='loki.cache')
    def some_method(a, b):
        time.sleep(2)
        return a + b


    @cache
    def some_next():
        pass


    print(some_method(31, 76))
