import unittest
from typing import Tuple


def algorithm(input: Tuple[Tuple]) -> int:
    result = 0
    (n, m) = input[0]
    print(f'n: {n}, m: {m}')
    vertices = [i for i in range(1, n+1)]

    cycles = []
    for vertex in vertices:
        # get all relations for this vertex
        unique_adjacent_vertices = get_unique_adjacent_vertices(input, vertex)
        print(f'Unique vertices of vertex {vertex}: {unique_adjacent_vertices}')
        for candidate in unique_adjacent_vertices:
            path = [vertex, candidate]
            print(path)
            next_vertices = get_unique_adjacent_vertices(input, candidate)
            filtered_next_vertices = [v for v in next_vertices if v not in path]
            print('filtered next vertices: ', filtered_next_vertices)
            for filtered_next_vertex in filtered_next_vertices:
                candidate_path = path + [filtered_next_vertex]
                print('candidate path: ', candidate_path)
                is_final_vertex_adjacent_to_initial_vertex = (candidate_path[-1], vertex) in input[1:] or (vertex, candidate_path[-1]) in input[1:]
                if len(candidate_path) >= 3 and is_final_vertex_adjacent_to_initial_vertex:
                    potential_loop = candidate_path + [vertex]
                    if potential_loop not in cycles and potential_loop[::-1] not in cycles:
                        print('potential loop: ', potential_loop)
                        if not is_potential_loop_a_repeat(cycles, potential_loop):
                            cycles.append(candidate_path + [vertex])
            print('\n')
    print(cycles)
    result = len(cycles)
    return result

def is_potential_loop_a_repeat(cycles, potential_loop) -> bool:
    print('cycles: ', cycles, 'potential loop: ', potential_loop)
    for cycle in cycles:
        print('cycle: ', cycle, 'loop', potential_loop)
        if cycle[0] in potential_loop:
            for i in range(len(potential_loop)):
                if potential_loop[i] == cycle[0]:
                        shifted_potential = potential_loop[i:] + potential_loop[:i]
                        if shifted_potential == cycle:
                            return True
    return False


def generate_all_possible_paths(input: Tuple[Tuple]) -> list:
    number_of_edges = input[0][1]
    number_of_vertices = input[0][0]
    edges_remaining = number_of_edges




def is_path_possible(path: list, input: Tuple[Tuple]) -> bool:
    if len(path) < 3:
        return False
    if path[0] != path[-1]:
        return False

    # for vertex in path:
    #     for (source, destination) in input[1:]:
    #         if vertex



def get_unique_adjacent_vertices(input, vertex):
    from_to_adjacent_vertices = [adj for (source, adj) in input[1:] if source == vertex]
    to_from_adjacent_vertices = [adj for (adj, source) in input[1:] if source == vertex]
    unique_adjacent_vertices = list(set(from_to_adjacent_vertices + to_from_adjacent_vertices))
    return unique_adjacent_vertices


class TestSolution(unittest.TestCase):

    def test_zero_case(self):
        provided_input = (
            (0, 0),
            )
        expected_output = 0
        self.assertEqual(algorithm(provided_input), expected_output)

    def test_minimum_case(self):
        provided_input = (
            (3, 3),
            (1, 2),
            (1, 3),
            (2, 3)
            )
        expected_output = 1
        self.assertEqual(algorithm(provided_input), expected_output)

    def test_square_case(self):
        provided_input = (
            (4, 4),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 1),
            )
        expected_output = 1
        self.assertEqual(algorithm(provided_input), expected_output)

    def test_moderate_case(self):
        provided_input = (
            (4, 5),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 1),
            (1, 3),
            )
        expected_output = 3
        self.assertEqual(algorithm(provided_input), expected_output)

    def test_provided_case(self):
        provided_input = (
            (4, 6),
            (1, 2),
            (1, 3),
            (1, 4),
            (2, 3),
            (2, 4),
            (3, 4),
            )
        expected_output = 7
        self.assertEqual(algorithm(provided_input), expected_output)


if __name__ == '__main__':


    # for case in (
    #     [],
    #     [1],
    #     [1, 2],
    #     [1, 2, 3],
    #     [1, 2, 3, 1],
    #     [4, 4, 1, 2, 4],
    #     [4, 1, 4, 2, 4],
    #     [1,2,3,4,1],
    #     [1,2,1],
    # ):
    #     print(is_valid(case), case)



    def is_valid(path: 'list[int]', provided_input: Tuple[Tuple]) -> Tuple[bool, str]:
        max_length = provided_input[0][1]
        if not path:
            return False, 'Path is empty'
        if not is_cycle(path):
            return False, 'Path is not a cycle'
        elif not is_at_least_three_vertices(path):
            return False, 'Path is not at least three vertices'
        elif not is_not_repeating_vertex(path):
            return False, 'Path is repeating a vertex'
        elif not is_path_made_up_of_real_edges(path, provided_input):
            return False, 'Path is not made up of real edges'
        elif is_too_long(path, max_length):
            return False, 'Path is too long'
        return True, 'Path is valid'


    def is_cycle(path: 'list[int]') -> bool:
        return path[0] == path[-1]

    def is_at_least_three_vertices(path: 'list[int]') -> bool:
        return len(path) >= 4

    def is_not_repeating_vertex(path: 'list[int]') -> bool:
        return len(set(path[:-1])) == len(path[:-1])

    def is_path_made_up_of_real_edges(path: 'list[int]', input: 'list[tuple[int, int]]') -> bool:
        return not any(
            (path[i], path[i + 1]) not in input[1:]
            and (path[i + 1], path[i]) not in input[1:]
            for i in range(len(path) - 1)
        )

    def is_too_long(path: 'list[int]', max_length: int) -> bool:
        return len(path) > max_length + 1


    provided_input = (
        (4, 5),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 1),
        (1, 3),
        )

    def generate_all_permutations(path: 'list[int]', provided_input: Tuple[Tuple]) -> 'list[list[int]]':
        if len(path) == provided_input[0][0]:
            return [path + [path[0]]]
        results = []
        # add one vertex
        for vertex in range(1, provided_input[0][0] + 1):
            if vertex not in path:
                results.extend(generate_all_permutations(path + [vertex], provided_input))
        if len(path) >= 3:
            results.append(path + [path[0]])
        return results

    cases = (generate_all_permutations([], provided_input))

    def filter_candidates(cases: 'list[list[int]]') -> 'list[list[int]]':
        # first, remove any candidates that are reverses of other candidates
        non_reversable = []
        for case in cases:
            if case[::-1] not in non_reversable:
                non_reversable.append(case)

        filtered = []
        for case in non_reversable:
        # for each case
            for other_case in non_reversable:
            # for each other case
                if case != other_case:
                    non_first_vertex_case = case[1:]
                    non_first_vertex_other_case = other_case[1:]
                    if all([
                        non_first_vertex_case != non_first_vertex_other_case,
                        non_first_vertex_case != non_first_vertex_other_case[::-1],
                        ]):
                        if case not in filtered:
                            filtered.append(case)
                # trim first vertex of case
                # trim first vertex of other case
                # if the two trimmed cases are equal
                    # remove the case break
                # if the case is equal to the reverse of the other case
                    # remove the case break
            # include the case

        return filtered

        # # second, remove any candidates whose body (- first and last vertices) is a subset of another candidate
        subsets = []
        for case in non_reversable:
            for other_case in non_reversable:
                if case != other_case and case[1:-1] != reversed(other_case[1:-1]):
                    if case not in subsets:
                        subsets.append(case)

        return subsets

    filtered_candidates = filter_candidates(cases)

    # cases = (
    #     [1, 2, 3, 4, 1],
    #     [],
    #     [1,2,3,4],
    #     [1,2,3,2],
    #     [1,2,1],
    #     [4,1,3,4],
    #     [4,1,1,3,4],
    #     [4,1,3,1,4],
    #     [4,1,4,2,4],
    #     [4,1,2,3,1,4],
    # )
    for case in filtered_candidates:
        result, message = is_valid(case, provided_input)
        if result:
            print(result, message, case)


    # TestSolution().test_minimum_case()
    # TestSolution().test_provided_case()
    # print('All tests passed!')

