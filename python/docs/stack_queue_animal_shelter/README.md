# Stack Queue Animal Shelter
Create a class AnimalShelter while holds only dogs and cats. Shelter operates using FIFO behavior.
Implement: 
- enqueue with an argument animal (either dog or cat object). Must have species and name property.
- dequeue with argument preference (either dog or cat object) and returns prefered animal object. If pref is not dog or cat, then return NULL

## Whiteboard Process
[Stack Queue Animal Shelter](/python/docs/stack_queue_animal_shelter/Stack%20Queue%20Animal%20Shelter.jpg)

## Approach & Efficiency
- Enqueue has an O(1) because it simply places the new animal at the front and that behavior doesn't change regardless of thesize of the animal shelter

- Dequeue has an O(1) only if the requested species in the front animal. It's O(n) if the requested species is not in the front and the algorithm has to traverse through the animal list

## Solution
Available at: [Stack Queue Animal Shelter](/python/code_challenges/stack_queue_animal_shelter.py)