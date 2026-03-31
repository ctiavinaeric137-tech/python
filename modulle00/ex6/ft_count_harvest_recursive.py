# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tiarakot <tiarakot@student.42antananarivo  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/30 14:47:34 by tiarakot          #+#    #+#              #
#    Updated: 2026/03/30 14:55:24 by tiarakot         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	helper(days, day):
	if (day > days):
		print("Harvest time!")
		return
	else :
		print("Day", day)
		helper(days, day + 1)
		

def	ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))
	helper(days, 1)
