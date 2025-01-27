from api import ProvideQApi

# Choose local or server
# base_url = "http://localhost:8080"
base_url = "https://betaapi.provideq.kit.edu"
# base_url = "https://api.provideq.kit.edu"

api = ProvideQApi(base_url)

def test_vrp_with_kmeans_and_lkh():
    vrp_input = """
    NAME : small sample
    TYPE : CVRP
    CAPACITY : 3
    DIMENSION : 5
    EDGE_WEIGHT_TYPE : EUC_2D
    NODE_COORD_SECTION
    1 0.0 0.0
    2 2.0 1.0
    3 1.0 -2.0
    4 -4.0 1.0
    5 -2.0 -3.0
    DEMAND_SECTION
    1 0
    2 1
    3 1
    4 1
    5 1
    DEPOT_SECTION
    1
    -1
    """

    solver_per_type = {
        "vrp": lambda: "edu.kit.provideq.toolbox.vrp.solvers.LkhVrpSolver",
        "cluster-vrp": lambda: "edu.kit.provideq.toolbox.vrp.clusterer.KmeansClusterer",
        "tsp": lambda: "edu.kit.provideq.toolbox.tsp.solvers.LkhTspSolver",
        "qubo": lambda: "edu.kit.provideq.toolbox.qubo.solvers.QrispVrpSolver"
    }

    settings_per_solver_id = {
        "edu.kit.provideq.toolbox.vrp.clusterer.KmeansClusterer": lambda: [
            {
                "name": "Cluster Number",
                "type": "INTEGER",
                "required": False,
                "description": "",
                "min": 1,
                "max": 1000,
                "value": 3,
            }
        ],
    }

    api.solve("vrp", vrp_input, "edu.kit.provideq.toolbox.vrp.solvers.ClusterAndSolveVrpSolver", solver_per_type, settings_per_solver_id)

def test_vrp_with_kmeans_and_qrisp_grover():
    # Read file content at 
    vrp_input = 

    vrp_input = """
    NAME : CMT1
    COMMENT : 524.61
    TYPE : CVRP
    DIMENSION : 51
    EDGE_WEIGHT_TYPE : EUC_2D
    CAPACITY : 160
    NODE_COORD_SECTION
    1 30.00000 40.00000
    2 37.00000 52.00000
    3 49.00000 49.00000
    4 52.00000 64.00000
    5 20.00000 26.00000
    6 40.00000 30.00000
    7 21.00000 47.00000
    8 17.00000 63.00000
    9 31.00000 62.00000
    10 52.00000 33.00000
    11 51.00000 21.00000
    12 42.00000 41.00000
    13 31.00000 32.00000
    14 5.00000 25.00000
    15 12.00000 42.00000
    16 36.00000 16.00000
    17 52.00000 41.00000
    18 27.00000 23.00000
    19 17.00000 33.00000
    20 13.00000 13.00000
    21 57.00000 58.00000
    22 62.00000 42.00000
    23 42.00000 57.00000
    24 16.00000 57.00000
    25 8.00000 52.00000
    26 7.00000 38.00000
    27 27.00000 68.00000
    28 30.00000 48.00000
    29 43.00000 67.00000
    30 58.00000 48.00000
    31 58.00000 27.00000
    32 37.00000 69.00000
    33 38.00000 46.00000
    34 46.00000 10.00000
    35 61.00000 33.00000
    36 62.00000 63.00000
    37 63.00000 69.00000
    38 32.00000 22.00000
    39 45.00000 35.00000
    40 59.00000 15.00000
    41 5.00000 6.00000
    42 10.00000 17.00000
    43 21.00000 10.00000
    44 5.00000 64.00000
    45 30.00000 15.00000
    46 39.00000 10.00000
    47 32.00000 39.00000
    48 25.00000 32.00000
    49 25.00000 55.00000
    50 48.00000 28.00000
    51 56.00000 37.00000
    DEMAND_SECTION
    1 0
    2 7
    3 30
    4 16
    5 9
    6 21
    7 15
    8 19
    9 23
    10 11
    11 5
    12 19
    13 29
    14 23
    15 21
    16 10
    17 15
    18 3
    19 41
    20 9
    21 28
    22 8
    23 8
    24 16
    25 10
    26 28
    27 7
    28 15
    29 14
    30 6
    31 19
    32 11
    33 12
    34 23
    35 26
    36 17
    37 6
    38 9
    39 15
    40 14
    41 7
    42 27
    43 13
    44 11
    45 16
    46 10
    47 5
    48 25
    49 17
    50 18
    51 10
    DEPOT_SECTION
    1
    -1
    """

    solver_per_type = {
        "vrp": lambda: "edu.kit.provideq.toolbox.vrp.solvers.QrispVrpSolver",
        "cluster-vrp": lambda: "edu.kit.provideq.toolbox.vrp.clusterer.KmeansClusterer",
    }

    settings_per_solver_id = {
        "edu.kit.provideq.toolbox.vrp.clusterer.KmeansClusterer": lambda: [
            {
                "name": "Cluster Number",
                "type": "INTEGER",
                "required": False,
                "description": "",
                "min": 1,
                "max": 1000,
                "value": 3,
            }
        ],
    }

    api.solve("vrp", vrp_input, "edu.kit.provideq.toolbox.vrp.solvers.ClusterAndSolveVrpSolver", solver_per_type, settings_per_solver_id)

def test_tsp_with_lkh():
    tsp_input = """
    NAME : small sample
    TYPE : TSP
    DIMENSION : 5
    EDGE_WEIGHT_TYPE : EUC_2D
    NODE_COORD_SECTION
    1 0.0 0.0
    2 2.0 1.0
    3 1.0 -2.0
    4 -4.0 1.0
    5 -2.0 -3.0
    EOF
    """

    solver_per_type = {}

    settings_per_solver_id = {}

    api.solve("tsp", tsp_input, "edu.kit.provideq.toolbox.tsp.solvers.LkhTspSolver", solver_per_type, settings_per_solver_id)

def test_tsp_with_dwave_qubo():
    tsp_input = """
    NAME : small sample
    TYPE : TSP
    DIMENSION : 5
    EDGE_WEIGHT_TYPE : EUC_2D
    NODE_COORD_SECTION
    1 0.0 0.0
    2 2.0 1.0
    3 1.0 -2.0
    4 -4.0 1.0
    5 -2.0 -3.0
    EOF
    """

    solver_per_type = {
        "qubo": lambda: "edu.kit.provideq.toolbox.qubo.solvers.DwaveQuboSolver",
    }

    settings_per_solver_id = {
        "edu.kit.provideq.toolbox.qubo.solvers.DwaveQuboSolver": lambda: [
            {
                "name": "D-Wave Token",
                "type": "TEXT",
                "required": False,
                "description": "",
                "text": "",
            },
            {
                "name": "Annealing Method",
                "type": "SELECT",
                "required": False,
                "description": "",
                "options": [],
                "selectedOption": "sim",
            }
        ],
    }

    api.solve("tsp", tsp_input, "edu.kit.provideq.toolbox.tsp.solvers.QuboTspSolver", solver_per_type, settings_per_solver_id)

# test_vrp_with_kmeans_and_lkh()
test_vrp_with_kmeans_and_qrisp_grover()

# test_tsp_with_lkh()
# test_tsp_with_dwave_qubo()
