# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tiarakot <tiarakot@student.42antananarivo  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/30 14:37:12 by tiarakot          #+#    #+#              #
#    Updated: 2026/03/30 14:39:49 by tiarakot         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_water_reminder():
	days = int(input("Days since last watering: "))
	if (days > 2):
		print("Water the plants!")
	else :
		print("Plants are fine")

