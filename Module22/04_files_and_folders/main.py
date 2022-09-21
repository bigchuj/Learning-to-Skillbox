# TODO здесь писать код

import os


def quantity_files_and_total_size(
    way,
    size_files=0,
    quantity_sub_dir=0,
    quantity_files=0
):

    list_dir = os.listdir(way)

    for elem in list_dir:

        new_way = os.path.join(way, elem)

        if os.path.isdir(new_way):

            vars = quantity_files_and_total_size(
                new_way,
                quantity_sub_dir=(quantity_sub_dir + 1)
            )

            size_files += vars[0]
            quantity_sub_dir = vars[1]
            quantity_files += vars[2]

        else:

            quantity_files += 1
            size_files += os.path.getsize(new_way)

    return size_files, quantity_sub_dir, quantity_files


dirrectory_way = input("Введите путь до каталога: ").strip()
# столкнулся с проблемой при проверке, когда при копировании пути
# до коталога, может копироваться пробел как в начале, так и в конце
# поэтому здесь strip() будет являться защитой, удаляя пробелы в начале и в конце
size_files,\
    quantity_sub_dir,\
    quantity_files = quantity_files_and_total_size(dirrectory_way)
size_files /= 1024

print("Размер каталога (в Кб):", size_files)
print("Количество подкаталогов:", quantity_sub_dir)
print("Количество файлов:", quantity_files)
