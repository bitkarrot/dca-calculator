# {%favicon%}
# {%css%}
# {%metas%}
# <title>{%title%}</title>


content_string = """
<!DOCTYPE html>
<html>
    <head>
    <link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css\">
    </head>
    <body>
        <nav class="container-fluid" style="border-bottom-style:solid; border-color: rgb(66, 66, 66); border-width: 0.1px">
              <ul>
            <li><strong>Brand</strong></li>
          </ul>
          <ul>
            <li><a href="#">Link</a></li>
            <li><a href="#">Link</a></li>
          </ul>
        </nav>       
        <main class="container">
         <section id="preview">
            <h1>Let's DCA Bitcoin!</h1>
                <p>
                Sed ultricies dolor non ante vulputate hendrerit. Vivamus sit amet suscipit sapien. Nulla
                iaculis eros a elit pharetra egestas.
                </p>

            {%app_entry%}
        </section>
        </main>
        <section id="footer">
       <footer class="container">
            {%config%}
            {%scripts%}
            {%renderer%}
          <div> 
              Built with <a href="https://picocss.com"> Pico </a> • 
              <a href="https://github.com/bitkarrot/"> Source </a>
          </div>
          </section>
        </footer>
    </body>
</html>
"""


form_string = """<form>
      <div class="grid">
          <label for="text">
            Amount
            <input
              type="number"
              name="Amount"
              placeholder="100"
            />
            </label>
             <!-- Select -->
          <label for="select">Frequency
          <select id="select" name="select" required>
            <option value="Weekly" selected>Select…</option>
            <option value="Daily">Daily</option>
            <option value="Weekly">Weekly</option>
          </select>
          </label>
            </label>
            <!-- Date-->
            <label for="date"
              >Start Date
              <input type="date" id="startdate" name="startdate" />
            </label>
            <label>
            <!-- Date-->
            <label for="date"
              >End Date
              <input type="date" id="enddate" name="enddate" />
            </label>
            <label>
            </div>
            <div class="grid">
            <button type="submit">LFG!</button>
            </div>
        </form>"""
