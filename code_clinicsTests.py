import unittest, sys, test_base
from io import StringIO
from test_base import captured_io


class AppTestCases(unittest.TestCase):
    def test_volunteer_exists(self):
        with captured_io(StringIO('Demo\nPython demo\n9\n0')) as (out,err):
            import volunteer_slot
            output = out.getvalue().strip()
        
        self.assertTrue('volunteer_slot' in sys.modules, "MODULE volunteer_slot.py must be present.")
        
        
    def test_update_exist(self):
        with captured_io(StringIO('Demo\nPython demo\n9\n0')) as (out,err):
            import update_event
            output = out.getvalue().strip()
            self.assertTrue('update_event' in sys.modules, "MODULE update_event.py must be present.")
            
    def test_run_exist(self):
        import run
        self.assertTrue("run" in sys.modules, "MODULE run.py must be present.")
        
    def test_list_events_exist(self):
        with captured_io(StringIO('')) as (out,err):
            import list_events
            output = out.getvalue().strip()
            self.assertTrue('list_events' in sys.modules, "MODULE list_events.py must be present.")

            
    def test_info_exist(self):
        with captured_io(StringIO('')) as (out,err):
            import info
            output = out.getvalue().strip()
            self.assertTrue('info' in sys.modules, "MODULE info.py must be present.")
            
    def test_cancel_volunteering(self):
        with captured_io(StringIO('Demo\nPython demo\n9\n0')) as (out,err):
            import cancel_volunteering
            output = out.getvalue().strip()
            self.assertTrue("cancel_volunteering" in sys.modules, "MODULE cancel_volunteering.py must be present.")
    
    def test_cancel_booking_exist(self):
        with captured_io(StringIO('Demo\nPython demo\n9\n0')) as (out,err):
            import cancel_booking
            output = out.getvalue().strip()
            self.assertTrue('cancel_booking' in sys.modules, "MODULE cancel_booking.py must be present.")
            
    
    def test_cal_setup_exist(self):
        with captured_io(StringIO('Demo\nPython demo\n9\n0')) as (out,err):
            import cal_setup
            output = out.getvalue().strip()
            self.assertTrue('cal_setup' in sys.modules, "MODULE cal_setup.py must be present.")
            
            
    def test_booking_exist(self):
        with captured_io(StringIO('Demo\nPython demo\n9\n0')) as (out,err):
            import booking 
            output = out.getvalue().strip()
            self.assertTrue('booking' in sys.modules, "MODULE booking.py must be present.")
            
if __name__ == "__main__":
    unittest.main()