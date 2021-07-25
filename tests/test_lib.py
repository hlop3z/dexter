import dexter

import lib_a, lib_b

app = dexter.group(lib_a, lib_b)
#plugins = dexter.get_keys(lib_a, lib_b)

print("")
print("#public_actions")
print(
    list(app.keys())
)

print("\n")
print("#lib_a")
lib_a.plugin_a.myfunc()
lib_a.plugin_a.Aclass.test()
lib_a.plugin_b.Bclass.test()

print("\n")
print("#lib_b")
app['lib_b.plugin_a.myfunc']()
app['lib_b.plugin_a.Aclass'].test()
app['lib_b.plugin_b.Bclass'].test()