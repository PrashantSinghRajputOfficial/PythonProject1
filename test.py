# # {
# #  "cells": [
# #   {
# #    "cell_type": "code",
# #    "execution_count": null,
# #    "metadata": {},
# #    "outputs": [
# #     {
# #      "name": "stdout",
# #      "output_type": "stream",
# #      "text": [
# #       "List a: [1, 2, 3, 4, 5]\n",
# #       "List b: ['A', 'B', 'C', 'D', 'E']\n",
# #       "List c: [1, 'A', 2, 'B', 3, 'C', 4, 'D', 5, 'E']\n",
# #       "Multi-Dimensional List using List c: [{'A': [1]}, {'B': [2]}, {'C': [3]}, {'D': [4]}, {'E': [5]}]\n",
# #       "New List c reverted back from multi-dimensional list: [1, 'A', 2, 'B', 3, 'C', 4, 'D', 5, 'E']\n",
# #       "New List a reverted back from new List c: [1, 2, 3, 4, 5]\n",
# #       "New List b reverted back from new List c: ['A', 'B', 'C', 'D', 'E']\n"
# #      ]
# #     }
# #    ],
# #    "source": [
# #     "a=[1,2,3,4,5]\n",
# #     "b=['A','B','C','D','E']\n",
# #     "c=[]\n",
# #     "\n",
# #     "for i in range (len(a)):\n",
# #     "    c.append(a[i])\n",
# #     "    c.append(b[i])\n",
# #     "\n",
# #     "print(f'List a: {a}\\nList b: {b}\\nList c: {c}')\n",
# #     "\n",
# #     "multi_dimensional_c=[{c[i+1]: [c[i]]}for i in range (0,len(c),2)]\n",
# #     "\n",
# #     "print(f'Multi-Dimensional List using List c: {multi_dimensional_c}')\n",
# #     "\n",
# #     "new_c=[]\n",
# #     "for elements in multi_dimensional_c:\n",
# #     "    for key, value in elements.items():\n",
# #     "        new_c.append(value[0])\n",
# #     "        new_c.append(key)\n",
# #     "\n",
# #     "print(f'New List c reverted back from multi-dimensional list: {new_c}')\n",
# #     "\n",
# #     "new_a=new_c[0::2]\n",
# #     "new_b=new_c[1::2]\n",
# #     "\n",
# #     "print(f'New List a reverted back from new List c: {new_a}\\nNew List b reverted back from new List c: {new_b}')"
# #    ]
# #   },
# #   {
# #    "cell_type": "code",
# #    "execution_count": 5,
# #    "metadata": {},
# #    "outputs": [
# #     {
# #      "name": "stdout",
# #      "output_type": "stream",
# #      "text": [
# #       "Name in reverse: aytidA\n"
# #      ]
# #     }
# #    ],
# #    "source": [
# #     "name='Aditya'\n",
# #     "name_reversed=name[::-1]\n",
# #     "print(f'Name in reverse: {name_reversed}')"
# #    ]
# #   }
# #  ],
# #  "metadata": {
# #   "kernelspec": {
# #    "display_name": "base",
# #    "language": "python",
# #    "name": "python3"
# #   },
# #   "language_info": {
# #    "codemirror_mode": {
# #     "name": "ipython",
# #     "version": 3
# #    },
# #    "file_extension": ".py",
# #    "mimetype": "text/x-python",
# #    "name": "python",
# #    "nbconvert_exporter": "python",
# #    "pygments_lexer": "ipython3",
# #    "version": "3.9.13"
# #   }
# #  },
# #  "nbformat": 4,
# #  "nbformat_minor": 2
# # }

# # Creating a Fruits list
# fruits = [
#     "Apple",
#     "Orange",
#     "Mango",
#     "Banana",
#     "Papaya"
# ]

# fruits2 = [
#     1,
#     2,
#     3,
#     4,
#     5
# ]

# fruits3 = []
# # Get Fruit name in sequencial order using for loop

# for index,value in enumerate(fruits,start=1):
#     for index2,value2 in enumerate(fruits2,start=1):
#         if (index == index2):
#             fruits3.append([value,value2])
# print(frui)
my_list = [2,3,4]

if not my_list:  
    print("The list is empty!")  
else:  
    print("The list is not empty!")  
