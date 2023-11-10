from f_one_core_utilities import send_email_v3
from utils import launch_calculator, add_numbers, create_email_payload

def main():
    # Launch the calculator
    launch_calculator()

    # Perform addition
    result = add_numbers(3, 3)

    # Print the result
    print(f"The result of 3 + 3 is {result}")

    # Create email payload
    payload = create_email_payload(result)

    # Send email
    email_successfully_sent, msg_id = send_email_v3(payload)

if __name__ == "__main__":
    main()
