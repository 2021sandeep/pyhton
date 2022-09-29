football_points={"wins":3,"draws":1,"losses":0}
        def football(no_wins,no_draws,no_losses):
            no_points=no_wins*football_points["wins"]+no_draws*football_points["draws"]+no_losses*football_points["losses"]
                return (no_points)

                print(football(3,4,2))
                print(football(5,0,2))
                print(football(0,0,1))
