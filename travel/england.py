class EnglandPackage:
    def detail(self):
        print("[Vacation to England 10 days] London, Wales, Scotland $5,000")

if __name__ == "__main__":
    print("england module will run directly")
    print("This statement will operate when module runs directly")
    trip_to = EnglandPackage()
    trip_to.detail()
else:
    print("england is called from external source")