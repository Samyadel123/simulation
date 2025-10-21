from NewsDailyerSim.Simulation import NewsDialerSim

Random_Numbers = "8604323973662489769738244509185544151217547860494050807514530346261157653666113026204150168566597714921688253019271869999649912765209262528239119364630733154590005460333741583464394017346455470977878004210870844448475377577534141509890804004597244111997084593503694814216017058457"


if __name__ == "__main__":
    sim = NewsDialerSim(Random_Numbers)
    sim.simulate(30)
    sim.save_results("Simulation_Results")
    print("Simulation completed and results saved to 'Simulation_Results'")
    sim = NewsDialerSim(Random_Numbers)
    sim.simulate(70)
    sim.save_results("Simulation_Results_70days.csv")
    print("Simulation completed and results saved to 'Simulation_Results_70days.csv'")
    sim = NewsDialerSim(Random_Numbers)
    sim.simulate(100)
    sim.save_results("Simulation_Results_100days.csv")
