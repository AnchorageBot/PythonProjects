
[What are the basic Mathematical Axioms? - Tom Rocks Maths](https://youtu.be/9Efsz2hIpxE?si=Rsse-8HTjXBrEmb-)

[Axiom of Choice: Can you make infinitely many choices? - Zundamon's Theorem](https://youtu.be/86W8WkDnG2A?si=A9pM3TJHdZI3sqcE)

[ZF and axiomatic set theory - bodirsky](https://youtu.be/2U0IeyM0KGk?si=Gbu1TWAJLQN1m4T6)

Zermelo-Fraenkel Axioms with Equations

1. **Axiom of Extensionality (Identity)**:  
   ∀A ∀B (A = B ↔ ∀C (C ∈ A ↔ C ∈ B))

2. **Axiom of Foundation (Regularity)**:  
   ∀A (A ≠ ∅ → ∃B (B ∈ A ∧ B ∩ A = ∅))

3. **Axiom of Specification (Comprehension)**:  
   ∀A ∃B ∀x (x ∈ B ↔ x ∈ A ∧ φ(x))

4. **Axiom of Pairing**:  
   ∀a ∀b ∃C ∀x (x ∈ C ↔ x = a ∨ x = b)

5. **Axiom of Union**:  
   ∀A ∃B ∀x (x ∈ B ↔ ∃C (C ∈ A ∧ x ∈ C))

6. **Axiom of Power Set**:  
   ∀A ∃B ∀x (x ∈ B ↔ x ⊆ A)

7. **Axiom of Infinity**:  
   ∃A (∅ ∈ A ∧ ∀x (x ∈ A → x ∪ {x} ∈ A))

8. **Axiom Schema of Replacement**:  
   If F is a function, then:  
   ∀A ∃B ∀y (y ∈ B ↔ ∃x (x ∈ A ∧ y = F(x)))

9. **Axiom of Choice** (added to form ZFC):  
   ∀A (∅ ∉ A ∧ ∀x,y ∈ A (x ≠ y → x ∩ y = ∅) → ∃C ∀x ∈ A (|C ∩ x| = 1))
