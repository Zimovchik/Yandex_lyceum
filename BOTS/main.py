# import vk_api
# from passwords import LOGIN, PASSWORD
#
#
# def main():
#     login, password = LOGIN, PASSWORD
#     vk_session = vk_api.VkApi(login, password)
#     try:
#         vk_session.auth(token_only=True)
#     except vk_api.AuthError as error_msg:
#         print(error_msg)
#         return
#     vk = vk_session.get_api()
#     # Используем метод wall.get
#     response = vk.wall.get(count=3, offset=0)
#     print(response)
#     if response['items']:
#         for i in response['items']:
#             print(i["date"], )
#
#
# if __name__ == '__main__':
#     main()
a = 'немужчина,аоблаковштанах'
print(*a, sep='\n')
b = 'h+nu)~(4em>,>q6i>xQ3s>m>y'
print(*set([a[i] + " - " + b[i] for i in range(len(a))]), sep='\n')