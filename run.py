from salvaft.package2 import (
    generate_password,
    generate_guid,
    generate_credit_card_number,
    generate_object_id,
    generate_pin_number,
)
from salvaft.package1 import (
    generate_password as generate_password2,
    generate_guid as generate_guid2,
    generate_credit_card_number as generate_credit_card_number2,
    generate_object_id as generate_object_id2,
    generate_pin_number as generate_pin_number2,
)


print(generate_password2(length=8))

print(generate_guid2())

print(generate_credit_card_number2(length=16))

print(str(generate_pin_number2(length=4)))

print(generate_object_id2())


print(generate_password(length=8))

print(generate_guid())

print(generate_credit_card_number(length=16))

print(str(generate_pin_number(length=4)))

print(generate_object_id())
