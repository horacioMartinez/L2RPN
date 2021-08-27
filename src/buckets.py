# Create buckets!

# First try: normalized? rho of each line, max rho?. Bus for each load/gen/line_or/line_ex. If line disconnected line_or and line_ex in bus -1.

RHO_BUCKET_STEP_PERCENTAGE = 0.15
MIN_RHO = 0.4
MAX_RHO = 5

# NUM_LINES = 59
TOPOLOGY_VECTOR_LENGTH = 177

# Bus is -1/1/2


def generate_rho_buckets_ceilings():
    bucket_ceilings = [MIN_RHO]
    while bucket_ceilings[-1] < MAX_RHO:
        bucket_ceilings.append(bucket_ceilings[-1] + bucket_ceilings[-1] * RHO_BUCKET_STEP_PERCENTAGE)
    return bucket_ceilings


def num_rho_buckets():
    bucket_ceilings = generate_rho_buckets_ceilings()
    return len(bucket_ceilings) + 1  # Last bucket is > max


def rho_to_bucket(rho):
    bucket_ceilings = generate_rho_buckets_ceilings()
    for i in range(0, len(bucket_ceilings)):
        if bucket_ceilings[i] > rho:
            return i
    return len(bucket_ceilings)


def bus_to_bucket(bus):
    assert bus == -1 or bus == 1 or bus == 2
    if bus == -1:
        return 0
    return bus  # Maybe we should encode 1 as 0 since it is more common ??.


def bucket_hash_of_observation(observation):
    lines_rho = observation.rho
    rho_buckets = []
    for line_rho in lines_rho:
        rho_buckets.append(rho_to_bucket(line_rho))

    topology_vector = observation.topo_vect
    assert len(topology_vector) == TOPOLOGY_VECTOR_LENGTH

    bus_buckets = []
    for bus in topology_vector:
        bus_buckets.append(bus_to_bucket(bus))

    hash = "".join(map(str, rho_buckets + bus_buckets))
    return hash
