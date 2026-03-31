# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tiarakot <tiarakot@student.42antananarivo  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/30 14:04:18 by tiarakot          #+#    #+#              #
#    Updated: 2026/03/30 14:16:27 by tiarakot         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_harvest_total():
	day = 1
	total = 0
	while (day <= 3):
			day_harvest = int(input("Day " + day + " harvest: "))
			day += 1
			total += day_harvest
	print("Total harvest: " + total)
