
# in the original version LeafNode rendered image html with a closing </img> but image html is self closing
# I updated the LeafNode by adding a third branch to to_html() method :
# if self.value == "":
#            return f"<{self.tag}{self.props_to_html()}>"
# but the change has not been tested
# TO DO :
# 1. make sure that image html is rendered correctly without the closing </img>
# 2. check that the Solution files on boot.dev contain correct code for images (code in the LeafNode child class is not correct)
# 3. check that the test suit on boot.dev test for self closing image html
# 4. submit error messages on boot.dev
