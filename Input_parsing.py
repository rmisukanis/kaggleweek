import random

# Read files
def parse_input_file(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    
    photo_sum = int(lines[0])  # Sum of photos
    photos = []

    for i, line in enumerate(lines[1:]):
        parts = line.split()
        photo_type = parts[0]
        tags = set(parts[2:])  # Ignore tags number, extract directly the set of tags
        photos.append({'id': i, 'type': photo_type, 'tags': tags})
    
    return photos

# Create frameglasses
def build_frameglasses(photos):
    frameglasses = []
    used_ids = set()

    # All "L" are treaded as a frameglass
    for photo in photos:
        if photo['type'] == 'L':
            frameglasses.append({'ids': [photo['id']], 'tags': photo['tags']})
            used_ids.add(photo['id'])

    # For "P", random pair
    portraits = [p for p in photos if p['type'] == 'P' and p['id'] not in used_ids]
    random.shuffle(portraits)

    for i in range(0, len(portraits) - 1, 2):
        p1, p2 = portraits[i], portraits[i + 1]
        combined_tags = p1['tags'].union(p2['tags'])
        frameglasses.append({'ids': [p1['id'], p2['id']], 'tags': combined_tags})
        used_ids.update([p1['id'], p2['id']])

    return frameglasses

# photos = parse_input_file('C:\\Users\\HUAWEI\\Desktop\\Msc_software_engineering\\S3\\kaggle_week\\data\\input\\110_oily_portraits.txt')
# frameglasses = build_frameglasses(photos)

random.shuffle(frameglasses)

# Print some frameglass result to see the structure
for fg in frameglasses[:5]:
    print("Frameglass IDs:", fg['ids'], "Tags:", fg['tags'])

def write_output_file(output_filename, total_photos, frameglasses):
    with open(output_filename, 'w') as f:
        f.write(f"{total_photos}\n")                # First line: Sum of photos
        f.write(f"{len(frameglasses)}\n")           # Second line: Frameglass numbers
        for fg in frameglasses:
            f.write(' '.join(map(str, fg['ids'])) + '\n')  # Each framglass' ID line

