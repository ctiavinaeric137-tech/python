# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tiarakot <tiarakot@student.42antananarivo  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/30 14:17:31 by tiarakot          #+#    #+#              #
#    Updated: 2026/03/30 14:35:24 by tiarakot         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_plant_age():
	age = int(input("Enter plant age in days: "))
	if (age > 60):
		print("Plants is ready to harvest!")
	else :
		print("Plant needs more time to grow.")
