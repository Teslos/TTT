import numpy as np

x = np.loadtxt('./TTT_Ti6Al4V_Malinov_endset.txt', comments='#', dtype='double', delimiter=',')

u, indices = np.unique(x[:, 1], axis=0, return_index=True)

np.savetxt('./TTT_Ti6Al4V_Malinov_endset_uniq.txt', x[indices], delimiter=',')




