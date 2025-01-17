"""
@file: global_example.py
@breif: global planner application examples
@author: Winter
@update: 2023.3.2
"""

from python_motion_planning.utils import Grid, Map, SearchFactory


if __name__ == '__main__':
    '''
    path searcher constructor
    '''
    search_factory = SearchFactory()

    '''
    graph search
    '''
    # build environment
    start = (50, 60)
    goal = (90, 70)
    env = Grid(120, 100)

    # creat planner
    planner = search_factory("a_star", start=start, goal=goal, env=env)

    # planner = search_factory("dijkstra", start=start, goal=goal, env=env)
    # planner = search_factory("gbfs", start=start, goal=goal, env=env)
    # planner = search_factory("theta_star", start=start, goal=goal, env=env)
    # planner = search_factory("lazy_theta_star", start=start, goal=goal, env=env)
    # planner = search_factory("s_theta_star", start=start, goal=goal, env=env)
    # planner = search_factory("jps", start=start, goal=goal, env=env)
    # planner = search_factory("d_star", start=start, goal=goal, env=env)
    # planner = search_factory("lpa_star", start=start, goal=goal, env=env)
    # planner = search_factory("d_star_lite", start=start, goal=goal, env=env)
    # planner = search_factory("voronoi", start=start, goal=goal, env=env, n_knn=4,
    #                             max_edge_len=10.0, inflation_r=1.0)

    # animation
    planner.run()

    # ========================================================

    '''
    sample search
    '''
    # # build environment
    # start = (18, 8)
    # goal = (37, 18)
    # env = Map(51, 31)

    # # creat planner
    # planner = search_factory("rrt", start=start, goal=goal, env=env)
    # planner = search_factory("rrt_connect", start=start, goal=goal, env=env)
    # planner = search_factory("rrt_star", start=start, goal=goal, env=env)
    # planner = search_factory("informed_rrt", start=start, goal=goal, env=env)

    # # animation
    # planner.run()

    # ========================================================

    '''
    evolutionary search
    '''
    # planner = search_factory("aco", start=start, goal=goal, env=env)
    #planner = search_factory("pso", start=start, goal=goal, env=env)
    #planner.run()