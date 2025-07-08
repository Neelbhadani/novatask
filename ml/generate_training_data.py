import json
import random
from faker import Faker

fake = Faker()

actions = ['register', 'create_work_order', 'add_tenant', 'delete_user', 'update_profile']
labels = ['allow', 'block', 'flag']

def generate_fake_example():
    action = random.choice(actions)
    data = {
        "email": fake.email(),
        "user_name": fake.user_name(),
        "title": fake.sentence(nb_words=4),
        "description": fake.text(max_nb_chars=100),
        "tenant_name": fake.company()
    }
    context = {
        "ip": fake.ipv4(),
        "device": random.choice(["Chrome", "Firefox", "Safari", "Edge"])
    }
    label = random.choice(labels)

    return {
        "action": action,
        "data": data,
        "user_context": context,
        "label": label
    }

def main():
    dataset = [generate_fake_example() for _ in range(100)]
    with open('data/novatask_training_data.json', 'w') as f:
        json.dump(dataset, f, indent=4)
    print("✅ Generated 100 training examples at '../data/novatask_training_data.json'")

if __name__ == "__main__":
    main()
