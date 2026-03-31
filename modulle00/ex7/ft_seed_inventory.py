# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tiarakot <tiarakot@student.42antananarivo  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/30 14:56:32 by tiarakot          #+#    #+#              #
#    Updated: 2026/03/30 15:13:04 by tiarakot         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_seed_inventory(seed_type: str, quantity: int, unity: str):
	seed_type_cap = seed_type.capitalize()
	if (unity == "packets"):
		print(seed_type_cap + " seeds: " + str(quantity) + " " + unity + " available")
	elif (unity == "grams"):
		print(seed_type_cap + " seeds: " + str(quantity) + " " + unity + " total")
	elif (unity == "area"):
		print(seed_type_cap + " seeds: "  + "covers " + str(quantity) + " sqare meters")
	else :
		print("Unknown unit type")
