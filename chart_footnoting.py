def split_string_by_length(text_to_split, line_length=150):
  '''This function will split text into lines (of a specified length)
  using the '\\n character.
  
  Why was this created?
  I was trying to create a footnote for a chart in Seaborn and the wrap property of plt.figtext wasn't doing what I needed.
  
  ==========
  params:
  ==========
  text_to_split : str
    This is the text that you want to split into lines
  line_length : int
    This is the maximum number of characters that you would like on each line.
    
  '''
  string_list = text_to_split.split(' ')
  lines = []
  current_string = ''
  
  while string_list:
    if len(current_string) + len(string_list[0]) <= line_length:
      current_string = current_string + string_list.pop(0) + ' '
      if len(string_list) == 0:
        lines.append(current_string)
        current_string = ''
      else:
        lines.append(current_string)
        current_string = ''
        
  return '\n'.join(lines)
