target_jump = int(input())
total_jumps = 0
unsuccessful_jump_counter = 0
first_target_jump = target_jump - 30
while True:
    jump = int(input())
    total_jumps += 1

    if jump > target_jump and first_target_jump >= target_jump:
        print(f"Tihomir succeeded, he jumped over {first_target_jump}cm after {total_jumps} jumps.")
        break

    elif jump > first_target_jump:
        first_target_jump += 5
        unsuccessful_jump_counter = 0
    else:
        unsuccessful_jump_counter += 1

    if unsuccessful_jump_counter == 3:
        print(f"Tihomir failed at {first_target_jump}cm after {total_jumps} jumps.")
        break


desired_height = int(input())
starting_height = desired_height - 30
jump_counter = 0
fail_counter = 0
while True:
    jump_try_height = int(input())
    jump_counter += 1
    if jump_try_height > starting_height:
        if jump_try_height > starting_height >= desired_height:
            print(f"Tihomir succeeded, he jumped over {starting_height}cm after {jump_counter} jumps.")
            break
        else:
            fail_counter = 0
            starting_height += 5
    else:
        fail_counter += 1

    if fail_counter >= 3:
        print(f"Tihomir failed at {starting_height}cm after {jump_counter} jumps.")
        break



