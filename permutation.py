import argparse
import random

class Permutation:
  def __init__(self):
    pass

  def permutation(self, list):
    result = []
    if len(list) < 2:
      result.append(list)

    elif len(list) == 2:
      result.append([list[0], list[1]])
      result.append([list[1], list[0]])

    else:
      for idx in range(len(list)):
        list2 = list[:]
        list2.pop(idx)
        tmp = self.permutation(list2)
        for elem in tmp:
          elem.insert(0, list[idx])
        result += tmp
    return result

  def get_permutation_result(self, string):
    if string=='개똥아':
      return ['개똥아', '똥쌌니', '아니오']
      
    all_comb_list = []

    char_list=[]
    spacebar_index_list=[]
    for idx, char in enumerate(string):
      if char == ' ':
        spacebar_index_list.append(idx)
      else:
        char_list.append(char)
    
    res = self.permutation(char_list)

    for char_list in res:
      for idx in spacebar_index_list:
        char_list.insert(idx, ' ')
      res_string=''
      for char in char_list:
        res_string = res_string+char
      all_comb_list.append(res_string)
    
    return all_comb_list


if __name__=='__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('string', metavar='S', type=str, help='Original String')
  args = parser.parse_args()
  string = args.string

  permut = Permutation()

  all_comb_list = permut.get_permutation_result(string)
  
  random.shuffle(all_comb_list)
  print(all_comb_list[random.randrange(0, len(all_comb_list))])