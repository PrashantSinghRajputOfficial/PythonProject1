# # # {
# # #  "cells": [
# # #   {
# # #    "cell_type": "code",
# # #    "execution_count": null,
# # #    "metadata": {},
# # #    "outputs": [
# # #     {
# # #      "name": "stdout",
# # #      "output_type": "stream",
# # #      "text": [
# # #       "List a: [1, 2, 3, 4, 5]\n",
# # #       "List b: ['A', 'B', 'C', 'D', 'E']\n",
# # #       "List c: [1, 'A', 2, 'B', 3, 'C', 4, 'D', 5, 'E']\n",
# # #       "Multi-Dimensional List using List c: [{'A': [1]}, {'B': [2]}, {'C': [3]}, {'D': [4]}, {'E': [5]}]\n",
# # #       "New List c reverted back from multi-dimensional list: [1, 'A', 2, 'B', 3, 'C', 4, 'D', 5, 'E']\n",
# # #       "New List a reverted back from new List c: [1, 2, 3, 4, 5]\n",
# # #       "New List b reverted back from new List c: ['A', 'B', 'C', 'D', 'E']\n"
# # #      ]
# # #     }
# # #    ],
# # #    "source": [
# # #     "a=[1,2,3,4,5]\n",
# # #     "b=['A','B','C','D','E']\n",
# # #     "c=[]\n",
# # #     "\n",
# # #     "for i in range (len(a)):\n",
# # #     "    c.append(a[i])\n",
# # #     "    c.append(b[i])\n",
# # #     "\n",
# # #     "print(f'List a: {a}\\nList b: {b}\\nList c: {c}')\n",
# # #     "\n",
# # #     "multi_dimensional_c=[{c[i+1]: [c[i]]}for i in range (0,len(c),2)]\n",
# # #     "\n",
# # #     "print(f'Multi-Dimensional List using List c: {multi_dimensional_c}')\n",
# # #     "\n",
# # #     "new_c=[]\n",
# # #     "for elements in multi_dimensional_c:\n",
# # #     "    for key, value in elements.items():\n",
# # #     "        new_c.append(value[0])\n",
# # #     "        new_c.append(key)\n",
# # #     "\n",
# # #     "print(f'New List c reverted back from multi-dimensional list: {new_c}')\n",
# # #     "\n",
# # #     "new_a=new_c[0::2]\n",
# # #     "new_b=new_c[1::2]\n",
# # #     "\n",
# # #     "print(f'New List a reverted back from new List c: {new_a}\\nNew List b reverted back from new List c: {new_b}')"
# # #    ]
# # #   },
# # #   {
# # #    "cell_type": "code",
# # #    "execution_count": 5,
# # #    "metadata": {},
# # #    "outputs": [
# # #     {
# # #      "name": "stdout",
# # #      "output_type": "stream",
# # #      "text": [
# # #       "Name in reverse: aytidA\n"
# # #      ]
# # #     }
# # #    ],
# # #    "source": [
# # #     "name='Aditya'\n",
# # #     "name_reversed=name[::-1]\n",
# # #     "print(f'Name in reverse: {name_reversed}')"
# # #    ]
# # #   }
# # #  ],
# # #  "metadata": {
# # #   "kernelspec": {
# # #    "display_name": "base",
# # #    "language": "python",
# # #    "name": "python3"
# # #   },
# # #   "language_info": {
# # #    "codemirror_mode": {
# # #     "name": "ipython",
# # #     "version": 3
# # #    },
# # #    "file_extension": ".py",
# # #    "mimetype": "text/x-python",
# # #    "name": "python",
# # #    "nbconvert_exporter": "python",
# # #    "pygments_lexer": "ipython3",
# # #    "version": "3.9.13"
# # #   }
# # #  },
# # #  "nbformat": 4,
# # #  "nbformat_minor": 2
# # # }

# # # Creating a Fruits list
# # fruits = [
# #     "Apple",
# #     "Orange",
# #     "Mango",
# #     "Banana",
# #     "Papaya"
# # ]

# # fruits2 = [
# #     1,
# #     2,
# #     3,
# #     4,
# #     5
# # ]

# # fruits3 = []
# # # Get Fruit name in sequencial order using for loop

# # for index,value in enumerate(fruits,start=1):
# #     for index2,value2 in enumerate(fruits2,start=1):
# #         if (index == index2):
# #             fruits3.append([value,value2])
# # print(frui)
# # my_list = [2,3,4]

# # if not my_list:  
# #     print("The list is empty!")  
# # else:  
# #     print("The list is not empty!")  

# # making function for giving place name of users given Wonders of the World
# while True:
#     qna1 = input("\nDo you want to know the name of any 'Wonders of the World' place? : ")
#     if qna1.lower() == "yes":
#         break
#     elif qna1.lower() == "no":
#         print("No worries! Maybe some other time. 😊")
#         exit()
#     else:
#         print("Please enter yes or no only")

# wonders_of_world = input("Enter 'Wonders of the World' name : ").lower()
# def name(names,place):
#     print(f"{names}, It 'Wonders of world' in {place}")
# def place_name(wonders_of_world):
#     match wonders_of_world :
#         case "amazon rainforest" :
#             name("Amazon Rainforest","South America")
#         case "halong bay" :
#             name("Halong Bay","Vietnam")
#         case "iguazu falls" :
#             name("Iguazu Falls","Argentina/Brazil")
#         case "jeju island" :
#             name("Jeju Island","South Korea")
#         case "komodo island" :
#             name("Komodo Island","Indonesia")
#         case "puerto princesa underground river" :
#             name("Puerto Princesa Underground River","Philippines")
#         case "table mountain" :
#             name("Table Mountain","South Africa")            
            
# Great Wall of China
# Address: Huairou District, Beijing 101406, China

# Petra
# Address: Wadi Musa, Ma'an Governorate, Jordan

# Christ the Redeemer
# Address: Parque Nacional da Tijuca - Alto da Boa Vista, Rio de Janeiro - RJ, 25946-455, Brazil

# Machu Picchu
# Address: Machu Picchu, 08680, Peru

# Chichen Itza
# Address: Tinum Municipality, Yucatán 97751, Mexico

# Roman Colosseum
# Address: Piazza del Colosseo, 1, 00184 Roma RM, Italy

# Taj Mahal
# Address: Dharmapuri, Forest Colony, Tajganj, Agra, Uttar Pradesh 282001, India
print()
print()