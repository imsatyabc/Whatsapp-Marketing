nums = open('data.txt').read()

numbers = nums.split('\n')

et = ''

for i,v in enumerate(numbers):
  et += '''
<tr>
  <td>
    '''+str(i+1)+'''
  </td>
  <td>
    '''+str(v)+'''
  </td>
  <td>
    <a href="https://api.whatsapp.com/send/?phone='''+str(v)+'''&text&app_absent=0" target="_blank" class="btn btn-primary btn-sm"> Open </a>
  </td>
</tr>
'''


open('final.html', 'w+').write(et)