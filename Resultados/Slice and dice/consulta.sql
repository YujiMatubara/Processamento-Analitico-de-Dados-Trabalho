SELECT "Data - FkData"."Mes" AS "Data - FkData__Mes", sum("public"."saude_fatos"."Registro_ocorrencia") AS "sum"
FROM "public"."saude_fatos"
LEFT JOIN "public"."data" "Data - FkData" ON "public"."saude_fatos"."fkData" = "Data - FkData"."pkData" LEFT JOIN "public"."saude_local" "Saude Local - FkLocal" ON "public"."saude_fatos"."fkLocal" = "Saude Local - FkLocal"."pkLocal"
WHERE ("Data - FkData"."DataCompleta" >= timestamp with time zone '2021-01-01 00:00:00.000-03:00'
   AND "Data - FkData"."DataCompleta" < timestamp with time zone '2022-01-01 00:00:00.000-03:00' AND "Saude Local - FkLocal"."Municipio" = 'SAO PAULO')
GROUP BY "Data - FkData"."Mes"
ORDER BY 
    CASE 
        WHEN "Data - FkData"."Mes" = '1' THEN 1
        WHEN "Data - FkData"."Mes" = '2' THEN 2
        WHEN "Data - FkData"."Mes" = '3' THEN 3
        WHEN "Data - FkData"."Mes" = '4' THEN 4
        WHEN "Data - FkData"."Mes" = '5' THEN 5
        WHEN "Data - FkData"."Mes" = '6' THEN 6
        WHEN "Data - FkData"."Mes" = '7' THEN 7
        WHEN "Data - FkData"."Mes" = '8' THEN 8
        WHEN "Data - FkData"."Mes" = '9' THEN 9
        WHEN "Data - FkData"."Mes" = '10' THEN 10
        WHEN "Data - FkData"."Mes" = '11' THEN 11
        WHEN "Data - FkData"."Mes" = '12' THEN 12
    END
ASC