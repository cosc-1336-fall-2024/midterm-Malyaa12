#DON'T MAKE CHANGES TO THIS FILE

#write tests for all the questions here
import unittest

def main():
    print("Discovering and running tests...")

    # Load all test cases from the 'tests' directory
    loader = unittest.TestLoader()
    test_suite = loader.discover('tests')

    # Run the test suite
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    # Summary of results
    if result.wasSuccessful():
        print("\nAll tests passed!")
    else:
        print(f"\n{len(result.failures)} test(s) failed.")
        print(f"{len(result.errors)} test(s) had errors.")

if __name__ == "__main__":
    main()
