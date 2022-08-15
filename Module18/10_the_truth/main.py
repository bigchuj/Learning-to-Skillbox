# TODO здесь писать код


def decode_text(txt_list):

    new_txt_list = []
    shift = 3

    for word in txt_list:
        temp_letter = []

        for i in word:
            # этим циклом мы добавляем во временный список новые символы по сдвигу Цезаря
            temp_letter.append(chr(ord(i) - 1))

        for i in range(shift):
            # этим циклом мы меняем символы местами, так как есть сдвиг внутри слов
            temp_letter[:0] += [temp_letter.pop()]

        if temp_letter[-1] == '.':
            # здесь добавляем сдвиг для второго цикла, так как с каждым предложением
            # сдвиг учеличивается на 1
            shift += 1

        new_txt_list.append(''.join(temp_letter))

    return ' '.join(new_txt_list)


text = """vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo 
jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui 
dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo 
otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up 
csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme 
wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg 
hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe 
sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo 
cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs 
uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf 
tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up 
bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh 
efbj .. fu(tm pe psfn gp tf"uip
"""

decryption_text = decode_text(text.split())

print(decryption_text)
# zen of Python https://peps.python.org/pep-0020/
# run command in IDE >>> import this
