import tkinter as tk
from tkintermapview import TkinterMapView
import geocoder

class MyLocationMap:
    def __init__(self, root):
        self.root = root
        self.root.title("My Location")
        self.root.geometry("800x600")
        
        # Get your current location first
        self.get_location()
        
        # Then show the map
        self.show_map()
    
    def get_location(self):
        """Get your current latitude and longitude"""
        try:
            g = geocoder.ip('me')
            if g.ok:
                self.lat, self.lng = g.latlng
            else:
                self.lat, self.lng = 0, 0  # Default to world view
        except:
            self.lat, self.lng = 0, 0
    
    def show_map(self):
        """Show the map with your location"""
        self.map = TkinterMapView(self.root, width=800, height=600)
        self.map.pack()
        
        # If we got your location, zoom to it
        if self.lat != 0 and self.lng != 0:
            self.map.set_position(self.lat, self.lng)
            self.map.set_zoom(15)
            self.map.set_marker(self.lat, self.lng, text="You are here!")
        else:
            # Show world view if location not found
            self.map.set_position(0, 0)
            self.map.set_zoom(1)
            tk.messagebox.showinfo("Notice", "Couldn't find your location automatically")

# Run the app
if __name__ == "__main__":    
 root = tk.Tk()
 app = MyLocationMap(root)
 root.mainloop()