site = {
	'html': {
		'head': {
			'title': 'Куплю/продам телефон недорого'
		},
		'body': {
			'h2': 'У нас самая низкая цена на iPhone',
			'div': 'Купить',
			'p': 'Продать'
		}
	}
}

# TODO здесь писать код

from copy import deepcopy

def site_out(sites):

    for key in sites.keys():
        print('Сайт для {}:'.format(key))
        line_str = str(sites[key])

        # как вывести структуру ------ >>>
        line_list = []
        count = 0
        for elem in line_str:
            if elem == "{":
                count += 1
                line_list.append(elem + "\n" + "    " * count)
            elif elem == "}":
                count -= 1
                line_list.append("\n" + "    " * count + elem)
            elif elem == ",":
                line_list.append(elem + "\n" + "   ")
                line_list.append("    " * (count - 1))
            else:
                line_list.append(elem)
        
        print("site =", "".join(line_list))
        line_list.clear()


def new_sites(site, count_site, sites=dict()):
    count_site -= 1
    name_product = input('Введите название продукта для нового сайта: ')
    site_copy = deepcopy(site)
    site_copy['html']['head']['title'] = 'Куплю/продам {} недорого'.format(name_product)
    site_copy['html']['body']['h2'] = 'У нас самая низкая цена на {}'.format(name_product)
    sites[name_product] = site_copy
    site_out(sites)

    if count_site:
        new_sites(site_copy, count_site, sites)


count_site = int(input('Сколько сайтов: '))

new_sites(site, count_site)
