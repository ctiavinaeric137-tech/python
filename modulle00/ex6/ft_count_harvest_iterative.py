# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tiarakot <tiarakot@student.42antananarivo  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/30 14:42:21 by tiarakot          #+#    #+#              #
#    Updated: 2026/03/30 14:46:53 by tiarakot         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_count_harvest_iterative():
	day = int(input("Days until harvest: "))
	day_count = 1
	while (day_count <= day):
		print("Day " + day_count)
		day_count += 1
	print("Harvest time!")
