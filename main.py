from graph import app

def main():
  opt = {
    'configurable': {
      'thread_id': '1'
    }
  }
  while (user_input := input('User: ')) != 'bye':
    for event in app.stream({'content': [('user', user_input)]}, opt):
      for value in event.values():
        print('DeepSeek: ', value['content'][0].content)

if __name__ == '__main__':
  main()