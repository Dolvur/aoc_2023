file = open("input.txt", "r")
input_text = file.read()
file.close()

seeds = []
mapping_chunks = []
location_numbers = []
chunks = input_text.split("\n\n")

seeds = [int(item) for item in chunks[0][7:].split(" ")]

for chunk in chunks[1:]:
    lines = chunk.splitlines()[1:]
    current_map = [list(map(int, item.split(" "))) for item in lines]
    mapping_chunks.append(current_map)

current_preconversion_values = seeds
for chunk_index, mapping_chunk in enumerate(mapping_chunks):
    for curr_preconv_i, curr_preconv_val in enumerate(current_preconversion_values):
        for mapping_array in mapping_chunk:
            dest_range_start, source_range_start, range_length = mapping_array
            dist_from_source = curr_preconv_val - source_range_start
            if dist_from_source >= 0 and dist_from_source <= range_length:
                current_preconversion_values[curr_preconv_i] = (
                    dest_range_start + dist_from_source
                )
                break
            # else: # No map (map to same number e.g. no need to convert)

lowest_location_value = min(current_preconversion_values)
print(lowest_location_value)
