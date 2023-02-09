-- sql script to list all bands with Glam rock as their main style
-- rank the result by their longevity

SELECT band_name, IFNULL(split) - IFNULL(formed) AS lifespan

FROM metal_bands WHERE style LIKE '%Glam rock%'

ORDER BY lifespan DESC
