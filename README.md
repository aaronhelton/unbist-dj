# unbist-dj

This is a web application that allows the creation/import and management of multilingual thesauri. As such, it implements a subset of SKOS Core to aid in C_UD operations via the admin. Available owl:Class definitions include skos:ConceptScheme, skos:Concept, and skos:Collection. Available owl:ObjectProperty definitions include skos:broader, skos:narrower, skos:related, skos:member, skos:inScheme, skos:hasTopConcept, and skos:topCocnceptOf. Available owl:DatatypeProperty definitions include skos:prefLabel', 'skos:altLabel', 'skos:hiddenLabel', 'skos:notation', 'skos:note', 'skos:changeNote', 'skos:definition', 'skos:editorialNote', 'skos:example', 'skos:historyNote', and 'skos:scopeNote'. 

The file 13.sql is a sample seed file containing an entire category of data. Keep in mind that, since this came from an existing thesaurus, some of the relationships will fail to resolve, and there will be errors running the SQL.

Search for the front-end (read-only) application is currently built to use Haystack with an Elasticsearch backend. This is functional in a basic sense, but its structure can definitely be improved. 

Among the goals of this application are:

 * Comprehensive search of concepts across their multilingual labels, scope notes, and spanning relationships.
 * Full and intuitive CRUD operations for Concepts, Concept Schemes, and Collections, including assignment and traversal of properties and object links.
 * Act as a starting point for additional semantic data aware applications, extending via a combination of published and custom ontologies, as appropriate.
