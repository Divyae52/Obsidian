
                 <span class="goup">..</span></a></td>
                             <td>&mdash;</td>
                             <td class="hideable">&mdash;</td>
                             <td class="hideable"></td>
                         </tr>
                 """)

    # sort dirs first
    sorted_entries = sorted(path_top_dir.glob(glob_patt), key=lambda p: (not p.is_dir(), p.name))

    entry: Path