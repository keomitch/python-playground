class PrimeChecker:
  def __init__(self):
    """Initialize prime checker with cache and statistics"""
    self.known_primes = {2, 3, 5, 7, 11, 13, 17, 19}
    self.known_composites = {1}  # Also cache composites for speed
    self.checks_count = 0
    self.cache_hits = 0

  def is_prime(self, n):
    """Check if a number is prime using cached results when possible"""
    self.checks_count += 1

    # Check cache first
    if n in self.known_primes:
      self.cache_hits += 1
      return True
    if n in self.known_composites:
      self.cache_hits += 1
      return False

    # Quick checks
    if n < 2:
      self.known_composites.add(n)
      return False
    if n == 2:
      self.known_primes.add(n)
      return True
    if n % 2 == 0:
      self.known_composites.add(n)
      return False

    # Main prime check (your original logic)
    limit = int(n**0.5) + 1
    for i in range(3, limit, 2):
      if n % i == 0:
        self.known_composites.add(n)
        return False

    # If we get here, it's prime - cache it!
    self.known_primes.add(n)
    return True

  def generate_primes(self, upper_bound):
    """Generate all primes up to upper_bound using Sieve of Eratosthenes"""
    # 1. Initialize the Sieve list
    # We only care about numbers up to upper_bound
    is_prime_list = [True] * (upper_bound + 1)
    is_prime_list[0] = is_prime_list[1] = False # 0 and 1 are not prime

    # 2. Run the Sieve
    limit = int(upper_bound**0.5) + 1
    for p in range(2, limit):
      # If is_prime_list[p] is not changed, then it is a prime
      if is_prime_list[p]:
        # Update all multiples of p starting from p*p
        for i in range(p * p, upper_bound + 1, p):
          is_prime_list[i] = False

    # 3. Collect results and update internal caches
    primes = []
    for n in range(2, upper_bound + 1):
      if is_prime_list[n]:
        primes.append(n)
        # Bulk add to prime cache
        self.known_primes.add(n)
      else:
        # Bulk add composites to cache
        self.known_composites.add(n)

    return primes

  def get_stats(self):
    """Get performance statistics"""
    total = self.checks_count
    hit_rate = (self.cache_hits / total * 100) if total > 0 else 0
    return {
      'total_checks': total,
      'cache_hits': self.cache_hits,
      'primes_cached': len(self.known_primes),
      'composites_cached': len(self.known_composites),
      'cache_hit_rate': f"{hit_rate:.1f}%"
    }

  def interactive_mode(self):
    """Run interactive prime checking session"""
    print("\n🎯 PRIME CHECKER (OOP Version)")
    print("Commands: [q]uit, [s]tats, show cached [p]rimes")
    print("Actions: [c]heck number, [g]enerate primes")

    while True:
      try:
        user_command = input("\nprimeChecker> ").strip().lower()

        match user_command:
          case 'q':
            print("Thanks for using Prime Checker!")
            break

          case 's':
            stats = self.get_stats()
            print("📊 Statistics:")
            for key, value in stats.items():
              print(f"  {key:<32}: {value}")

          case 'p':
            primes = sorted(self.known_primes)
            print(f"🔢 Cached primes: {primes}")

          case 'c':
            try:
              n = int(input("Enter a number to check: ").strip())

              if n == 1:
                print("  You have submitted")
                print("  the multipilicative identity,")
                print("  a natural number which is")
                print("  neither a prime nor a composite number.\n")
              elif self.is_prime(n):
                print(f"✅ {n} is PRIME")
              else:
                print(f"❌ {n} is COMPOSITE")

            except ValueError:
              print("Please enter a valid integer.")

          case 'g':
            try:
              bound = int(input("Enter a nunber for the upper bound: ").strip())
              if bound < 2:
                print("Bound must be 2 or greater.")
                continue

              print(f"Generating primes up to {bound} using Sieve...")
              primes = self.generate_primes(bound) # Calls the efficient Sieve

              print(f"Generated {len(primes)} primes:")
              print(*primes, sep=' ')

            except ValueError:
              print("Invalid input. Please enter an integer for the bound.")

          case _:
            # Handle invalid commands
            print(f"Invalid command: '{user_command}'. Please use c, g, p, s, or q.")

      except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        break
